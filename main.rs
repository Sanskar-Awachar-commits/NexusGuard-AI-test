use actix_web::{web, App, HttpResponse, HttpServer, Responder};

// VULNERABLE: Directly echoing user input into HTML
async fn vulnerable_greet(info: web::Path<String>) -> impl Responder {
    let user_input = info.into_inner();
    let html_content = format!("<h1>Hello, {}!</h1>", user_input);
    
    HttpResponse::Ok()
    .content_type("text/html; charset=utf-8")
    .body(html_content)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().route("/greet/{name}", web::get().to(vulnerable_greet))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
