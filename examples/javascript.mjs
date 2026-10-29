import { FanDuelClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new FanDuelClient({ apiKey });

  const casinoCategories = await client.casinoCategories({  });
  console.log("casinoCategories", casinoCategories);
  const racingTracks = await client.racingTracks({  });
  console.log("racingTracks", racingTracks);
