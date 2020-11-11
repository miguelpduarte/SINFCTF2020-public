FROM elixir:1.10-alpine

WORKDIR /app
ENV MIX_ENV=prod

# Copy mix.exs here
COPY private/wait_a_minute/mix.exs .
COPY private/wait_a_minute/mix.lock .

RUN mix local.rebar --force
RUN mix local.hex --force
RUN mix do deps.get, deps.compile

# Copy code here
COPY private/wait_a_minute .

RUN mix compile --warnings-as-errors

EXPOSE 8080
# Run stuff
CMD ["mix", "run", "--no-halt"]
