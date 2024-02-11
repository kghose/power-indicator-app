# Battery power panel indicator 

![](screenshot.png)

This is a very simple [Application Panel Indicator][1]. It shows the current
battery power drain by doing `cat /sys/class/power_supply/BAT0/power_now`
periodically and using that as the text of the indicator. It is based on
[this example][2].

[1]: https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators`
[2]: https://askubuntu.com/a/820858
