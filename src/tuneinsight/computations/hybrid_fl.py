from typing import Optional, Dict, Union
from datetime import datetime
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from tuneinsight.api.sdk import models
from tuneinsight.client.computations import ComputationRunner


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

        dataobjects = super().run_computation(comp = model, local = False, keyswitch = False, decrypt = False)

        return dataobjects

    def display_results(self, history):
        self.plot_timeline(history)

        print('Train loss:', round(history.train_losses[-1][-1], 4))
        print('Test loss:', round(history.test_losses[-1][-1], 4))
        print()
        print('Train accuracy:', round(history.train_accs[-1][-1], 4))
        print('Test accuracy:', round(history.test_accs[-1][-1], 4))
        print()
        print('Train f1:', round(history.train_f1_s[-1][-1], 4))
        print('Test f1:', round(history.test_f1_s[-1][-1], 4))

    def plot_timeline(self, history, timescale: bool = False):
        _, ax = plt.subplots(3, 1, figsize=(20, 12))

        agg_durations = [datetime.fromtimestamp(end/1000.0) - datetime.fromtimestamp(starts[0]/1000.0) for (starts, end) in zip(history.end_timestamps, history.init_timestamps[1:])]
        local_epochs_durations = [datetime.fromtimestamp(ends[-1]/1000.0) - datetime.fromtimestamp(start/1000.0) for (start, ends) in zip(history.init_timestamps, history.end_timestamps)]

        aggregation_width = 1
        points_timestamps = [datetime.fromtimestamp(x/1000.0) for starts, ends in zip(history.start_timestamps, history.end_timestamps) for x in [starts[0]] + ends]
        epochs = [list(range(len(x) + 1)) for x in history.start_timestamps]
        flat_epochs = [x+i*(len(sublist)-1 + aggregation_width) for i, sublist in enumerate(epochs) for x in sublist]

        x_points = points_timestamps if timescale else flat_epochs

        train_losses = [x for init, sub in zip(history.init_train_losses, history.train_losses) for x in [init] + sub]
        train_accs = [100*x for init, sub in zip(history.init_train_accs, history.train_accs) for x in [init] + sub]
        train_f1s = [x for init, sub in zip(history.init_train_f1_s, history.train_f1_s) for x in [init] + sub]
        test_losses = [x for init, sub in zip(history.init_test_losses, history.test_losses) for x in [init] + sub]
        test_accs = [100*x for init, sub in zip(history.init_test_accs, history.test_accs) for x in [init] + sub]
        test_f1s = [x for init, sub in zip(history.init_test_f1_s, history.test_f1_s) for x in [init] + sub]

        max_loss = max(train_losses + test_losses)

        loss_plot_limits = (-max_loss/10, max_loss*11/10)
        acc_plot_limits = (-10, 110)
        f1_plot_limits = (-0.1, 1.1)

        plot_axis(ax[0], x_points, train_losses, test_losses, loss_plot_limits, epochs, aggregation_width, 'Loss')
        plot_axis(ax[1], x_points, train_accs, test_accs, acc_plot_limits, epochs, aggregation_width, 'Accuracy (%)')
        plot_axis(ax[2], x_points, train_f1s, test_f1s, f1_plot_limits, epochs, aggregation_width, 'F1-score')

        for i, epoch in enumerate(epochs):
            n_epochs = len(epoch)-1
            epoch_start = i*(n_epochs+aggregation_width)
            epoch_end = i*(n_epochs+aggregation_width) + n_epochs
            epochs_list = ', '.join(list(map(str, range(i*n_epochs+1, i*n_epochs+n_epochs+1))))
            text = f'Epochs {epochs_list}\n{local_epochs_durations[i].seconds} sec.'
            plt.text((epoch_start+epoch_end)/2+0.2, 2*f1_plot_limits[0], text, rotation=90, fontsize=14, ha='right', va='top')

            if i < len(epochs)-1:
                agg_start = len(epoch)-1+i*(len(epoch)-1+aggregation_width)
                text = f'Aggregation: {agg_durations[i].seconds} sec.'
                plt.text(agg_start+aggregation_width*0.5, 2*f1_plot_limits[0], text, rotation=90, fontsize=14, ha='right', va='top')

def plot_axis(axis, x, y_train, y_test, ylims, epochs, aggregation_width, label):
    axis.set_ylim(ylims[0], ylims[1])
    axis.plot(x, y_train, marker='.', label='Train')
    axis.plot(x, y_test, marker='.', label='Validation')
    axis.grid(axis='y', linewidth=0.5)
    axis.xaxis.set_major_locator(MaxNLocator(integer=True))
    axis.set_ylabel(label)
    for i, epoch in enumerate(epochs[:-1]):
        agg_start = len(epoch)-1+i*(len(epoch)-1+aggregation_width)
        agg_end = (i+1)*(len(epoch)-1+aggregation_width)
        axis.axvspan(agg_start, agg_end, alpha=0.2, color='grey')
    axis.get_xaxis().set_ticks([])
    axis.legend()
