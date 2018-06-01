docker build -t image-hub:1.0 .
docker tag image-hub:1.0 docker02:35000/image-hub:1.0
docker push docker02:35000/image-hub:1.0
