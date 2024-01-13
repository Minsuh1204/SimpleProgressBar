# SimpleProgressBar
Easy to use terminal-based progress bar

Simple Usage
------------
```python
# test.py
import time
import SimpleProgressBar

pb = SimpleProgressBar.ProgressBar(100, "DevTest")
pb.show()
for i in range(1, 101):
    time.sleep(0.1)
    pb.update(i)
```
![simple usage](/images/simple_usage.gif)
