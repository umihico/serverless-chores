# EXAMPLE: sh set_ssm_param SLACK_TOKEN xoxp-00000000000000-abcdef
aws ssm put-parameter --name $1 --type "String" --region ap-northeast-1 --overwrite --value $2
