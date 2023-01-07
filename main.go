package main

import (
  "fmt"
  "net/http"
  "log"
);

var count = 0;

func main() {
  log.Println("Starting counter!");

  http.HandleFunc("/", showCountHandler);
  http.HandleFunc("/increment", incrementHandler);
  http.HandleFunc("/decrement", decrementHandler);

  log.Fatal(http.ListenAndServe(":80", nil));

}

func showCountHandler(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, "%d", count);
}

func incrementHandler(w http.ResponseWriter, req *http.Request) {
  count += 1;
  fmt.Fprintf(w, "Ok");
}

func decrementHandler(w http.ResponseWriter, req *http.Request) {
  count -= 1;
  fmt.Fprintf(w, "Ok");
}

