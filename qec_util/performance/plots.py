from typing import Optional

import numpy as np
import matplotlib.pyplot as plt


def plot_line_threshold(
    ax: plt.Axes,
    phys_prob: np.ndarray,
    log_prob: np.ndarray,
    log_prob_lower: Optional[np.ndarray] = None,
    log_prob_upper: Optional[np.ndarray] = None,
    label: Optional[str] = None,
    color: Optional[str] = "blue",
) -> plt.Axes:
    """Plots the logical error probability as a function of the physiscal
    error probability, including its upper and lower error bars.

    Parameters
    ----------
    ax
        Matplotlib axis in which to plot.
    phys_prob
        Physical error probabilities.
    log_prob
        Logical error probability.
    log_prob_lower
        Lower bound on the logical error probability uncertainty.
    log_prob_upper
        Upper bound on the logical error probability uncertainty.
    label
        Label for the data. By default, no label.
    color
        Color for the data. By default, blue.

    Returns
    -------
    ax
        Matplotlib axis.
    """
    ax.plot(phys_prob, log_prob, ".", color=color, label=label)
    if (log_prob_lower is not None) and (log_prob_upper is not None):
        ax.fill_between(
            phys_prob, log_prob_lower, log_prob_upper, color=color, alpha=0.1
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("physical error probability, $p$")
    ax.set_ylabel("logical error probability, $p_L$")
    if label is not None:
        ax.legend(loc="best")

    return ax
