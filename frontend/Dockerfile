FROM node:lts-alpine

WORKDIR /usr/src/app/frontend

COPY package*.json ./

RUN npm install



ENV HOST=0.0.0.0
ENV PORT=80

COPY . .

RUN npm run build
