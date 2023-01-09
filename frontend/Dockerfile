FROM node:18
# install vue-cli vue-cli-service
# RUN npm install -g @vue/cli
# RUN npm install -g @vue/cli-service-global

RUN mkdir src
WORKDIR /src
COPY . /src


RUN yarn install
RUN export NODE_OPTIONS=--openssl-legacy-provider && yarn run build

# ENV HOST 0.0.0.0
# EXPOSE 3000
# ENV NUXT_HOST=0.0.0.0
# RUN export NODE_OPTIONS=--openssl-legacy-provider
# # ENTRYPOINT export NODE_OPTIONS=--openssl-legacy-provider
# ENV NODE_OPTIONS=--openssl-legacy-provider
# CMD ["yarn", "dev"]

FROM nginx:alpine as production-build
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stahg 1
COPY --from=builder /src /usr/share/nginx/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]