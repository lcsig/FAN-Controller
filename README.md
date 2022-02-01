# FAN-Controller
MSI Laptop - A Simple Script to Change Fans Speed based on Temperatures. 

### Usage:
`sudo ./main.py <profileName.rw>`

### Profile Readings
- The first fan data is for CPU, the second fan is for GPU.
- Temperature in Celsius.
- FAN Speed in Percentage.

```
[Temperatures_1]
>WEC 0x69 0x0
>WEC 0x6A 0x2d
>WEC 0x6B 0x3C
>WEC 0x6C 0x46
>WEC 0x6D 0x50
>WEC 0x6E 0x5A
>WEC 0x6F 0x5F
----
[FanSpeeds_1]
>WEC 0x72 0x0
>WEC 0x73 0x32
>WEC 0x74 0x34
>WEC 0x75 0x3D
>WEC 0x76 0x47
>WEC 0x77 0x52
>WEC 0x78 0x5B
```

- If temp is > 0, then speed should be 0
- If temp is > 45, then speed should be 0x32 (50%).
- etc ...

### Notes 

Please, check [ISW](https://github.com/YoyPa/isw) for more advanced project.
