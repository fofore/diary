1.关于linux找不到.so：
LD_DEBUG=libs /usr/local/memcached/bin/memcached -v
调试看看是调用哪里的libs，
并且要找到现在的lib：
find / -name libevent-2.0.so.5

