[![license: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/dlouky/bmat_test_dlouky/blob/master/LICENSE)
# Musical Works Single View

This repository provides the code and instructions to deploy a `Works Single View` application to aggregate and reconcile musical metada from a CSV file to a [PostgreSQL](https://www.postgresql.org/) database. This application can also be used to query the database given an [ISWC](https://en.wikipedia.org/wiki/International_Standard_Musical_Work_Code).
<br><br>

## **Instructions**
1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker-compose](https://docs.docker.com/compose/install/).
1. Install [Git](https://github.com/git-guides/install-git).
1. Clone this repo and navigate into it:
    ```bash
    git clone https://github.com/dlouky/bmat_test_dlouky.git \
    && cd bmat_test_dlouky
    ```
1. Build Docker images and start containers.
    ```bash
    docker-compose up -d --build
    ```
1. Go to [http://localhost:8000/](http://localhost:8000/) in your browser. You will see the `Musical Work List` which shows Musical Works present in the PostgreSQL database. It is empty right now because it is the first time you run the app.
<br><br>

## **Part 1**
To import metadata from a CSV file, a [custom django-admin command](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/) has been created. In your terminal, execute:
```bash
docker exec -it bmat_test_dlouky bash -c "python manage.py import_csv ./metadata_csv/works_metadata.csv"
```

Go to http://localhost:8000/ again. Now the `Musical Work List` shows the reconcile works saved in PostgreSQL database with the metadata provided by the CSV file present in `/metadata_csv/works_metadata.csv`. To get raw JSON go to [http://localhost:8000/?format=json](http://localhost:8000/?format=json)

<br>

##### *Note 1: From here on, `metadata` refers to musical data in a CSV file and `works` refers to a record in the database for a specific musical work.* 

<br>

### Questions
1. **Describe brieﬂy the matching and reconciling method chosen.**
    * `Matching`: If *iswc* in metadata exists in a work or if *title* and at least one contributor from *contributors* list from metadata exists in a work.
    * `Reconciling`: If the work matched lacks `title` or `iswc`, they are completed by the `title` or `iswc` provided by metadata. In case there are diﬀerent sets of `contributors` from metadata and work, the union of them are used to update `contributors` of work.<br><br>

    Matching and reconciling are implemented in `bmat_app/utils/work_flow.py`. 

1. **We constantly receive metadata from our providers, how would you automatize the process?**
    
    I would implement a solution-oriented to cloud computing. I would create a Rest API that allows the provider to upload the files with metadata to `S3 on AWS` and I would enqueue the task in an `SQS` (Simple Queue Service). That way I would have the pending tasks there. With `Docker`, I would create a service that connects to SQS to read the task that contains the reference (ARN) to the file saved in S3. With that ARN, I would download the file to a local folder and run the `custom django-admin command` (in this case, if the file with metadata is a CSV, I would download it to the `/metadata_csv` folder and run the command mentioned in **PART 1**). In local I would create a `Bash script` that detects if a new file is downloaded and automatically execute the command.
<br><br>
## **Part 2**

* OPTION 1: Go to `http://localhost:8000/<iswc>` to get the work with specified *\<iswc\>* in JSON format. E.g. [http://localhost:8000/T9204649558/](http://localhost:8000/T9204649558/) or if you need raw JSON: [http://localhost:8000/T9204649558/?format=json](http://localhost:8000/T9204649558/?format=json) <br><br>
* OPTION 2: Go to [http://localhost:8000/search_iswc/](http://localhost:8000/search_iswc/) and enter the `iswc` in the form to query the `Works Single View` in order to get the work with that *iswc* in JSON format. 

If no work matches with the specified *iswc*, an empty JSON ([]) is returned.

### Questions
1. **Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?**

    No. Response time would be longer because of the database size.

1. **If not, what would you do to improve it?**

    In this particular case (using PostgreSQL) I would index the `iswc` column to do database searches more efficiently. This would improve the speed of the search for a record.
    
    If there were other possible scenarios, I would use a distributed file system (like HDFS), with a distributed cache (like Apache Ignite or Alluxio), that I would query with search engines like Apache Trino, Hive, Impala, Spark, or Drill deployed with Kubernetes. All of this configured on a cloud computing platform such as AWS.


<br>

##### *Note 2: Go to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with Username=dlouky and Password=dlouky to access the Django administrative interface.*

<br>

## **Testing**
Some tests have been made in `bmat_app/tests`, run the tests with:
```bash
docker exec -it bmat_test_dlouky bash -c "coverage run --omit '.venv/*' --source='.' manage.py test bmat_app -v 2 && coverage html"
``` 
To get a test report:
```bash
docker exec -it bmat_test_dlouky bash -c "coverage report --omit '.venv/*'"
```

## **Improvements**
Many improvements could be made to the project, some of these are listed below
1. Cover 100% of tests (see coverage report)
1. Create a frontend to make the tool more user friendly
1. Implement [security](https://docs.djangoproject.com/en/3.2/topics/security/)
1. Set environment variables via django-environ and database configration via DATABASE_URL. Use django-aws-secrets-manager to manage the secret values used by Django through AWS's SecretsManager service
1. For production, I would follow [this steps](https://realpython.com/development-and-deployment-of-cookiecutter-django-via-docker/) to deploy [Nginx](https://nginx.org/) as the web server along with [Gunicorn](https://gunicorn.org/) instead of Django’s single-threaded development server to run the server process.

## **Stop and remove all**
To stop and remove the Docker images and containers:
```bash
docker rm -f $(docker ps -qa) \
&& docker rmi -f $(docker images -qa)
```
Finally remove Docker named volumes and network
```bash
docker volume prune \
&& docker network prune
```

## **Authors**

* **Federico Manuel Dlouky** - *Initial work* - [dlouky](https://github.com/dlouky)

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details