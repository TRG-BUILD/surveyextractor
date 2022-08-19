# surveyextractor
Automation of SurveyXact download

Set .env for accessing survey-xact
```python
survey_user=
survey_password=
connection_string=postgresql+psycopg2://USER_NAME:PASSWORD@serveradd/database
```

# Install

```python setup.py install```

# Usage:

```shell
$ python create_tables.py -i SURVEY_ID
$ python update_table_api.py -i SURVEY_ID
```

## Cronjob
```bash
$ crontab -e
```
```
0 */12 * * * python /srv/surveyextractor/update_table_api.py -i SURVEY_ID >> /srv/surveyextractor/survey_log.log
0 */12 * * * python /srv/surveyextractor/update_table_api.py -i SURVEY_ID >> /srv/surveyextractor/survey_log.log
```

## API documentation
[https://documenter.getpostman.com/view/1760772/S1a33ni6](https://documenter.getpostman.com/)

