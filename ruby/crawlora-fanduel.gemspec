require_relative "lib/crawlora/fanduel/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-fanduel"
  spec.version = Crawlora::Fanduel::VERSION
  spec.summary = "FanDuel API client for Crawlora (72 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted FanDuel API. Covers public racing, casino catalogue, and research data across 72 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fanduel-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-fanduel", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-fanduel/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
