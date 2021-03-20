FROM node:latest
WORKDIR /svelte

COPY rollup.config.js ./
COPY package*.json ./
RUN npm i -g npm
RUN npm install

COPY . . 