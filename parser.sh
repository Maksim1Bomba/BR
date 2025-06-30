#!/bin/bash

check_mail() {
    local mail=$1
    local regex=$2
    if ! [ -z "$mail" ] && [[ "$mail" =~ $regex ]]; then
	return 0
    else
        return 1
    fi
}

replace() {
    local line=$1
    local regex=$2
    local service=$3
    local file=$4
    local fullRegex="${service}[[:space:]]${regex}"

    local escapedLine=$(printf '%s' "$line" | sed 's/[\/&]/\\&/g')

    echo $fullRegexEscaped $line $service $file

    sed -i "s|${fullRegex}|${service} ${escapedLine}|g" "$file"
    return 0
    
}

get_info() {
    local mail="" # build.sh and renew_cert.sh use mail
    local domain="" # build.sh, renew_cert.sh and services/nginx/nginx.conf use domain
    local username="" # build.sh, services/psql/Dockerfile and renew_cert.sh use username
    local passwordPsql="" # services/psql/Dockerfile and backend/Dockerfile use passwordPsql
    local fileBuild="build_test.sh"
    local filePsqlDocker="build.sh"
    local fileRenewCert="renew_cert.sh"
    local fileNginxDocker="services/nginx/Dockerfile"
    local fileNginxConfig="services/nginx/nginx.conf"
    local fileBackendDockerfile="backend/Dockerfile"
   
    local regexMail="[A-Za-z0-9._%+-]\+[@][A-Za-z]\+\.[A-Za-z]\+"
    local regexUni="[A-Za-z0-9._%+-:]\+"
    
    read -r -p "Enter your mail: " mail
    
    until check_mail "$mail" $regexMail
    do
	read -r -p "Reenter your mail, example@mail.com: " mail
    done
    
    replace "$mail" "$regexMail" "--email" "$fileBuild"
    replace "$mail" "$regexMail" "--email" "$fileRenewCert"

    read -r -p "Enter your domain: " domain
    
    replace "$domain" "$regexUni" "-d" "$fileBuild"
    replace "$domain" "$regexUni" "-d" "$fileRenewCert"
    replace "$domain" "$regexUni" "server_name" "$fileNginxConfig"
    
    read -r -p "Enter your username of linux group: " username
    
    replace "${username}:${username}" "$regexUni" "-R" "$fileBuild"
    replace "${username}:${username}" "$regexUni" "-R" "$filePsqlDockerfile"
    replace "${username}:${username}" "$regexUni" "-R" "$fileRenewCert"

    read -r -p "Enter password for postgres: " passwordPsql

    replace "$passwordPsql" "$regexUni" "POSTGRES_PASSWORD" "$filePsqlDockerfile"
    replace "$PasswordPsql" "$regexUni" "POSTGRES_PASSWORD" "$fileBackendDockerfile"
 }

if  [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    get_info
fi
