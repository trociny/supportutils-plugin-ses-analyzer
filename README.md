# supportutils-plugin-ses-analyzer
SES supportconfig analyzer

This is a collection of scripts for analyzing data collected by
supportconfig tool from supportutils package [1] with ses plugin (a
plugin to gather data from SUSE Enterprise Storage systems) [1]
installed.

The scripts are collected in commands subdirectory and are supposed to
be run via `sesa` wrapper.

[1] https://en.opensuse.org/Supportutils
[2] https://github.com/SUSE/supportutils-plugin-ses

Usage example
-------------

```
$ git clone https://github.com/trociny/supportutils-plugin-ses-analyzer.git
$ cd supportutils-plugin-ses-analyzer
$ PATH=$(pwd):$PATH # add sesa script to the path
$ cd ~/arch/nts_node-admin01_190313_1515 # cd to a supportconfig collected data dir
$ sesa help
SES supportconfig analyzer

usage: sesa <command> [options] [args]

Commands:

  auth-list        print ceph auth list
  crash            print info about ceph daemon crashes
  df-detail        print ceph df detail
  health-detail    print ceph health detail
  historic_ops     print ceph daemon historic ops
  mon-dump         print ceph mon dump
  osd-df-tree      print ceph osd df tree
  osd-dump         print ceph osd dump
  perf             print ceph daemon perf
  pg-dump          print ceph pg dump
  report           print ceph report
  status           print ceph status
  version          print ceph version
$ sesa version
12.2.10-543-gfc6f0c7299
$ sesa status 
  cluster:
    id:     12391e76-abb9-34a8-934a-02e9d7691234
    health: HEALTH_WARN
            noscrub,nodeep-scrub flag(s) set
 
  services:
    mon: 3 daemons, quorum node-1,node-11,node-21
    mgr: node-11(active), standbys: node-21, node-1
    mds: cephfs-4/4/4 up  {0=node-2=up:active,1=node-12=up:active,2=node-4=up:active,3=node-22=up:active}, 4 up:standby-replay, 1 up:standby
    osd: 142 osds: 142 up, 142 in
         flags noscrub,nodeep-scrub
 
  data:
    pools:   2 pools, 5120 pgs
    objects: 2.76M objects, 10.5TiB
    usage:   31.1TiB used, 486TiB / 517TiB avail
    pgs:     5120 active+clean
 
  io:
    client:   2.79GiB/s rd, 1.14kop/s rd, 0op/s wr
 

$ sesa help historic_ops
usage: sesa historic_ops [-h] [-d] [-t] [mds.x|mon.x|osd.x]

print ceph daemon historic ops

positional arguments:
  mds.x|mon.x|osd.x     print ops for this daemon

optional arguments:
  -h, --help            show this help message and exit
  -d, --sort-by-daemon  sort by daemon
  -t, --sort-by-duration
                        sort by duration

$ sesa historic_ops -t |head
osd.49   0.050 2019-03-13 15:15:31.098414 osd_op(client.66034.0:28591902 1.55c 1:3aa5c1ff:::10000000bff.0000008a:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.4    0.049 2019-03-13 15:14:27.174137 osd_op(client.66034.0:28562770 1.5ef 1:f7a56f52:::10000000c64.00000182:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.74   0.048 2019-03-13 15:11:56.825240 osd_op(client.66034.0:28494419 1.e43 1:c273d0db:::10000000c40.000001d7:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.4    0.047 2019-03-13 15:11:22.269074 osd_op(client.135917.0:29858700 1.c98 1:193e1ad0:::10000000c77.0000047a:head [read 0~3145728] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.22   0.047 2019-03-13 15:13:27.862401 osd_op(client.164631.0:30810546 1.55d 1:baa4d787:::10000000c3e.0000056a:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.22   0.046 2019-03-13 15:11:01.430463 osd_op(client.66034.0:28469295 1.27 1:e40349a7:::10000000c03.00000293:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.114  0.044 2019-03-13 15:14:44.084371 osd_op(client.164631.0:30850709 1.2b8 1:1d432e63:::10000000c23.0000048b:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.74   0.044 2019-03-13 15:12:25.173506 osd_op(client.135917.0:29889732 1.755 1:aaed5f58:::10000000c45.000003b4:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.139  0.042 2019-03-13 15:11:32.907149 osd_op(client.135917.0:29863745 1.d38 1:1cb067a2:::10000000c55.000000d4:head [read 0~4194304] snapc 0=[] ondisk+read+known_if_redirected e1131)
osd.102  0.042 2019-03-13 15:12:50.687053 osd_op(client.135917.0:29902353 1.be6 1:67d71df5:::10000000c71.000003ca:head [read 0~3145728] snapc 0=[] ondisk+read+known_if_redirected e1131)
$ sesa perf dump bluefs db_used_bytes -n
osd.102  407896064
osd.114  341835776
osd.124  440401920
osd.131  769654784
osd.139  378535936
osd.22   400556032
osd.35   797966336
osd.4    972029952
osd.49   488636416
osd.62   596639744
osd.74   538968064
osd.89   494927872
```

Adding a new command
--------------------

To add a new command create a script (executable) in
supportutils-plugin-ses-analyzer/commands subdirectory with the name
of the new command. The script may expect that at the moment of its
execution the `SES_SUPPORTCONFIG_DIR` environment variable is set to
the location of a supportconfig collected data dir, and use this
variable when looking for files. When run with `description` argument
the script should just print its one line description and exit. When
run with `help` argument the script should print its help screen and
exit. This is needed for `sesa help` to produce useful output. When
run with any other arguments (or without arguments) the script is
expected to do actual job, i.e. process the collected data in some way
and produce some useful output.