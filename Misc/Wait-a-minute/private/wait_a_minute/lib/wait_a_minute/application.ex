defmodule WaitAMinute.Application do
  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  @moduledoc false

  use Application

  def start(_type, _args) do
    children = [
      # Starts a worker by calling: WaitAMinute.Worker.start_link(arg)
      # {WaitAMinute.Worker, arg}
      {Plug.Cowboy, scheme: :http, plug: WaitAMinute.Router, options: [port: 8080]}
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: WaitAMinute.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
