from typing import Optional, Dict, Union, List
from datetime import datetime
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from tuneinsight.api.sdk.api.api_dataobject import get_data_object
from tuneinsight.api.sdk import models
from tuneinsight.api.sdk.types import  Response
from tuneinsight.client.validation import validate_response
from tuneinsight.client.dataobject import DataObject
from tuneinsight.client.computations import ComputationRunner
# from tuneinsight.client.diapason import Diapason


class HybridFL(ComputationRunner):
    def create_from_params(
            self,
            task_id: str,
            learning_params: models.HybridFLLearningParams,
            task_def: Optional[Dict[str, Union[str, int, float]]] = None,
        ):
        model = models.HybridFL(type=models.ComputationType.HYBRIDFL)
        model.task_id = task_id
        model.learning_params = learning_params

        if task_def is not None:
            model.task_def = json.dumps(task_def)

        model.project_id = self.project_id

        dataobjects = super().run_computation(
            comp = model,
            local = False,
            keyswitch = False,
            decrypt = False
        )

        return dataobjects

    def get_client_result(self, client) -> List[DataObject]:
        results = []
        computation = client.get_project(self.project_id).model.computations[0]

        for result in computation.results:
            response: Response[models.DataObject] = get_data_object.sync_detailed(client = client.client, data_object_id = result)
            validate_response(response)
            results.append(DataObject(model=response.parsed, client = client.client))

        return results

    def display_results(self, history):
        self.plot_timeline(history)

        init_train_losses = [x for x in history.init_train_losses if x is not None]
        init_train_accs = [x for x in history.init_train_accs if x is not None]
        init_train_f1_s = [x for x in history.init_train_f1_s if x is not None]

        init_test_losses = [x for x in history.init_test_losses if x is not None]
        init_test_accs = [x for x in history.init_test_accs if x is not None]
        init_test_f1_s = [x for x in history.init_test_f1_s if x is not None]

        print('Train loss:', round(init_train_losses[-1], 4))
        print('Test loss:', round(init_test_losses[-1], 4))
        print()
        print('Train accuracy:', round(init_train_accs[-1], 4))
        print('Test accuracy:', round(init_test_accs[-1], 4))
        print()
        print('Train f1:', round(init_train_f1_s[-1], 4))
        print('Test f1:', round(init_test_f1_s[-1], 4))

    @staticmethod
    def plot_timeline(history):
        _, ax = plt.subplots(3, 1, figsize=(20, 12))

        init_timestamps = [x for x in history.init_timestamps if x is not None]
        start_timestamps = [x for x in history.start_timestamps if x is not None]
        end_timestamps = [x for x in history.end_timestamps if x is not None]

        init_train_losses = [x for x in history.init_train_losses if x is not None]
        train_losses = [x for x in history.train_losses if x is not None]
        init_train_accs = [x for x in history.init_train_accs if x is not None]
        train_accs = [x for x in history.train_accs if x is not None]
        init_train_f1_s = [x for x in history.init_train_f1_s if x is not None]
        train_f1_s = [x for x in history.train_f1_s if x is not None]

        init_test_losses = [x for x in history.init_test_losses if x is not None]
        test_losses = [x for x in history.test_losses if x is not None]
        init_test_accs = [x for x in history.init_test_accs if x is not None]
        test_accs = [x for x in history.test_accs if x is not None]
        init_test_f1_s = [x for x in history.init_test_f1_s if x is not None]
        test_f1_s = [x for x in history.test_f1_s if x is not None]

        agg_durations = [datetime.fromtimestamp(end/1000.0) - datetime.fromtimestamp(starts[0]/1000.0) for (starts, end) in zip(end_timestamps, init_timestamps[1:])]
        local_epochs_durations = [datetime.fromtimestamp(ends[-1]/1000.0) - datetime.fromtimestamp(start/1000.0) for (start, ends) in zip(init_timestamps, end_timestamps)]

        aggregation_width = 1
        epochs = [list(range(len(x) + 1)) for x in start_timestamps]
        flat_epochs = [x+i*(len(sublist)-1 + aggregation_width) for i, sublist in enumerate(epochs) for x in sublist]
        flat_epochs = flat_epochs + [flat_epochs[-1]+aggregation_width] # adds last aggregation

        x_points = flat_epochs

        train_losses = [x for init, sub in zip(init_train_losses, train_losses) for x in [init] + sub] + [init_train_losses[-1]]
        train_accs = [100*x for init, sub in zip(init_train_accs, train_accs) for x in [init] + sub] + [100*init_train_accs[-1]]
        train_f1s = [x for init, sub in zip(init_train_f1_s, train_f1_s) for x in [init] + sub] + [init_train_f1_s[-1]]
        test_losses = [x for init, sub in zip(init_test_losses, test_losses) for x in [init] + sub] + [init_test_losses[-1]]
        test_accs = [100*x for init, sub in zip(init_test_accs, test_accs) for x in [init] + sub] + [100*init_test_accs[-1]]
        test_f1s = [x for init, sub in zip(init_test_f1_s, test_f1_s) for x in [init] + sub] + [init_test_f1_s[-1]]

        max_loss = max(train_losses + test_losses)

        loss_plot_limits = (-max_loss/10, max_loss*11/10)
        acc_plot_limits = (-10, 110)
        f1_plot_limits = (-0.1, 1.1)

        plot_axis(ax[0], x_points, train_losses, test_losses, loss_plot_limits, epochs, aggregation_width, 'Loss')
        plot_axis(ax[1], x_points, train_accs, test_accs, acc_plot_limits, epochs, aggregation_width, 'Accuracy (%)')
        plot_axis(ax[2], x_points, train_f1s, test_f1s, f1_plot_limits, epochs, aggregation_width, 'F1-score')

        # Display time information below graph
        for i, epoch in enumerate(epochs):
            n_epochs = len(epoch)-1
            epoch_start = i*(n_epochs+aggregation_width)
            epoch_end = i*(n_epochs+aggregation_width) + n_epochs
            epochs_list = ', '.join(list(map(str, range(i*n_epochs+1, i*n_epochs+n_epochs+1))))
            text = f'Epochs {epochs_list}\n{local_epochs_durations[i].seconds} sec.'
            plt.text((epoch_start+epoch_end)/2+0.2, 2*f1_plot_limits[0], text, rotation=90, fontsize=14, ha='right', va='top')

            agg_start = len(epoch)-1+i*(len(epoch)-1+aggregation_width)
            text = f'Aggregation: {agg_durations[i].seconds} sec.'
            plt.text(agg_start+aggregation_width*0.5, 2*f1_plot_limits[0], text, rotation=90, fontsize=14, ha='right', va='top')

def plot_axis(axis, x, y_train, y_test, ylims, epochs, aggregation_width, label):
    axis.set_ylim(ylims[0], ylims[1])
    axis.yaxis.tick_right()
    axis.plot(x, y_train, marker='.', label='Train')
    axis.plot(x, y_test, marker='.', label='Validation')
    axis.grid(axis='y', linewidth=0.5)
    axis.xaxis.set_major_locator(MaxNLocator(integer=True))
    axis.set_ylabel(label)
    for i, epoch in enumerate(epochs):
        agg_start = len(epoch)-1+i*(len(epoch)-1+aggregation_width)
        agg_end = (i+1)*(len(epoch)-1+aggregation_width)
        axis.axvspan(agg_start, agg_end, alpha=0.2, color='grey')
    axis.get_xaxis().set_ticks([])
    axis.legend()
