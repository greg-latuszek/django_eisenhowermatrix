# Build development env on Ubuntu

## install docker
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce
sudo systemctl status docker
sudo usermod -aG docker ${USER}
```

## mailhog
Download & start it
```bash
docker pull mailhog/mailhog:v1.0.1
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog:v1.0.1
```
To see emails at MailHog jump to `http://127.0.0.1:8025/`
