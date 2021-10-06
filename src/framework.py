from matplotlib import pyplot as plt
import matplotlib.ticker as tck

plt.rcParams.update({
    "text.usetex": True,
    "font.size": 10,
    "axes.titley": 1.0,
    "font.family": "lmodern",
    "axes.titlelocation": "left",
    "axes.titlepad": -14,
    "legend.fancybox": False
})

N_MAX = [6, 8, 10, 12]

sequences = [
    [8, 5, 3.75, 3.5],
    [7.5, 4.75, 3.5, 3.25],
    [7, 4.5, 3.25, 3]
]

# Figure
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["63768D", "8AC6D0", "B8F3FF"])
fig.set_size_inches(4, 3.25)
for seq in sequences:
  ax.plot(N_MAX, seq, "d")


# Styling and Printing
ax.yaxis.set_minor_locator(tck.AutoMinorLocator(5))
ax.tick_params(axis="both", which="both", direction="in")
ax.grid(axis="both", color="lightgrey", linestyle=":")
ax.set_xlabel(r"$N_\mathrm{max}$")
ax.set_xlim(5, 13)
ax.set_ylim(2.5, 8.5)
ax.set_xticks(N_MAX)
ax.set_ylabel("Energy in MeV")
fig.savefig("media/dataflow.pdf",
            bbox_inches="tight", pad_inches=0)
