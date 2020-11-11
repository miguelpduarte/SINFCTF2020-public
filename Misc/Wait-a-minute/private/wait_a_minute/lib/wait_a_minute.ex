defmodule WaitAMinute do
  @flag File.read!("flag.txt") |> String.trim()

  def flag do
    @flag
  end
end
