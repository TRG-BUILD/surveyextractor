#!/bin/bash
cd "$(dirname "$(realpath "$0")")";
. $HOME/miniconda3/bin/activate base
python daily_briefing.py -c ../easemailing/jobcfg.json  >> survey_log2.log
