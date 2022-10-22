FROM node:18-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
COPY . .

RUN npm install && \
    npm run build

# start app
CMD ["npm", "run", "preview"]