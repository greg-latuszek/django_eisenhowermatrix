# Containers

## docker compose v2
* rewritten Python --> Go
* user better standardized specification format: https://compose-spec.io/
* `docker-compose` --> `docker compose` (injects into docker as just subcommand)
* flag `--project-name` to group containers not by folder name
* repo in https://github.com/docker/compose/

### install
```bash
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
docker compose version
```

## dockerize django app
* building image
   * create `Dockerfile` for django
   * create `docker-compose.yml`
   * `docker compose build`
* starting at IP:port
   * `python manage.py runserver 0.0.0.0:8000`

## tricks
* env variables (including passwords)
   * put them in `.env` in same folder as `docker-compose.yml`
   * in `docker-compose.yml` just declare them but without values
   * `docker compose` will fill values from `.env`
   * put `.env` in `.gitignore`
* building all images and containers
    * `docker compose build`
* overwriting prod-file with dev-file (files union, last one wins)
    * `docker compose -f docker-compose.yml -f docker-compose.dev.yml up`
* jump into specific container of `docker-compose.yml`
   * `docker compose -f docker-compose.yml -f docker-compose.dev.yml run web bash` then you can check `env`
* stopping containers (leaving containers)
   * `docker compose -f docker-compose.yml -f docker-compose.dev.yml stop`
* destroying containers (leaving images)
   * `docker compose -f docker-compose.yml -f docker-compose.dev.yml down`

## Caution
* don't use alpine
   * not so secure
   * weak support - just few developers (see their github)
* if you have mounted volumes - like git repo for development
   * and something inside container will create files - f.ex. db migration
   * then new files are created as root
   * and before pushing to repo host ensure that you `sudo chown -R user:group folder`
      * may be done by git hooks
      * add yourself to sudoers to not be asked for password
