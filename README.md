# memtest_report

Python version of [memtest_report.cgi](https://gist.github.com/robinsmidsrod/f5b4c784d6b9a4d48f41).


## Steps to build and deploy
```
docker build -t stephenl03/memtest-report:0.1.0 .
docker tag stephenl03/memtest-report:0.1.0 stephenl03/memtest-report:latest
docker push stephenl03/memtest-report:latest
```