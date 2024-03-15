# Battery power panel indicator 

![](screenshot.png)

This is a very simple [Application Panel Indicator][1]. It shows the current
battery power drain by doing `cat /sys/class/power_supply/BAT0/power_now`
periodically and using that as the text of the indicator. It is based on
[this example][2].

Copy the indicator app (`battery-rate.py`) somewhere ("`/my/path`") and copy the 
desktop file (`power-indicator.desktop`) to `~/.local/share/applications` after 
changing the `Exec` entry to whatever "`/my/path`" is. [See this for 
details][3].

[1]: https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators`
[2]: https://askubuntu.com/a/820858
[3]: https://unix.stackexchange.com/a/103222
