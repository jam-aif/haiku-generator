# Cloudflare Deployment Guide

## Prerequisites
1. [Cloudflare account](https://dash.cloudflare.com/sign-up)
2. [Node.js installed](https://nodejs.org/)
3. API keys ready (OpenAI, Supabase)

## Deploy Steps

### 1. Install Wrangler CLI
```bash
npm install -g wrangler
```

### 2. Login to Cloudflare
```bash
wrangler login
```

### 3. Set Environment Variables
```bash
# Set your API keys in Cloudflare dashboard:
# Go to Workers & Pages > haiku-generator > Settings > Environment Variables

# Add these variables:
OPENAI_API_KEY=your_openai_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here
```

### 4. Deploy
```bash
# Deploy the worker
wrangler pages publish . --project-name=haiku-generator

# Or use npm script
npm run deploy
```

## Alternative: Manual Upload

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. Navigate to "Workers & Pages"
3. Click "Create Application" > "Pages" > "Upload Assets"
4. Upload these files:
   - `_worker.js` (main worker file)
   - `wrangler.toml` (configuration)
5. Set environment variables in dashboard
6. Deploy!

## Environment Variables Setup

In Cloudflare Dashboard:
1. Go to Workers & Pages
2. Select your project
3. Go to Settings > Environment Variables
4. Add:
   - `OPENAI_API_KEY`
   - `SUPABASE_URL`
   - `SUPABASE_KEY`

## Custom Domain (Optional)

1. Go to your project in Cloudflare Pages
2. Click "Custom Domains"
3. Add your domain
4. Update DNS records as instructed

Your haiku generator will be live at: `https://haiku-generator.pages.dev`