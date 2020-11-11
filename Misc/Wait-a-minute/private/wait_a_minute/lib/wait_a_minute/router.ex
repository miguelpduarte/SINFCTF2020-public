defmodule WaitAMinute.Router do
  use Plug.Router
  import Plug.Conn

  # So that we accept any way to get input, be it json, form stuff, etc.
  plug(Plug.Parsers, parsers: [:urlencoded, :multipart, :json], json_decoder: Jason)

  plug(Plug.Logger)
  plug(:match)
  plug(:dispatch)

  get "/" do
    send_resp(conn, 200, "POST me the flag!")
  end

  post "/" do
    # IO.inspect(conn.params)
    secret_flag = WaitAMinute.flag()
    secret_flag_size = String.length(secret_flag)
    flag = conn.params["flag"]

    if flag do
      n_equal =
        to_charlist(secret_flag)
        |> Enum.zip(to_charlist(flag))
        |> Enum.count(fn {test_char, flag_char} -> test_char == flag_char end)

      # send_resp(conn, 200, "got a flag #{flag}")
      # send_resp(conn, 200, "#{n_equal} characters are equal")

      # Sleep an extra 500ms for each right character
      Process.sleep(500 * n_equal)

      if String.length(flag) == secret_flag_size && n_equal == secret_flag_size do
        send_resp(conn, 200, "correct")
      else
        send_resp(conn, 200, "wrong")
      end
    else
      send_resp(conn, 400, "no flag!")
    end
  end

  match _ do
    send_resp(conn, 404, "nope")
  end
end
