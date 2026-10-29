use crawlora_fanduel::{
    Client, FanduelCasinoCategoriesParams, ModelFanduelCasinoCategoriesResponseDoc,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .fanduel
        .casino_categories(FanduelCasinoCategoriesParams {
            ..Default::default()
        })
        .await?;
    let data: ModelFanduelCasinoCategoriesResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
