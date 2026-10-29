import { FanDuelClient } from "../src/index.js";

const client = new FanDuelClient({ apiKey: "test-key" });
void client.casinoCategory({"category": "all-games"});
void client.request("fanduel-casino-category", {"category": "all-games"});
const streamResponse: Promise<Response> = client.request("fanduel-casino-category", {"category": "all-games"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("fanduel-casino-category", {"category": "all-games"}, { responseType: "stream" });
const directStream: Promise<Response> = client.casinoCategory({"category": "all-games"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("fanduel-casino-category", {"region": "mi", "category": "all-games", "q": "sample", "provider": "sample", "badge": "sample", "limit": 1, "offset": 1}, { responseType: "text" });
const rawText: Promise<string> = client.request("fanduel-casino-category", {"category": "all-games"}, { responseType: "text" });
void rawText;


void client.casinoCategories();
void client.request("fanduel-casino-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.casinoCategory();
