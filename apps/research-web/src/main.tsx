import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

type Result = { query: string; route: string; answer: string; warnings: string[]; citations: string[]; mode: string };
function App() {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState<Result | null>(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  async function submit(event: React.FormEvent) {
    event.preventDefault(); setLoading(true); setError(''); setResult(null);
    try {
      const response = await fetch('/api/v1/research', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ query }) });
      if (!response.ok) throw new Error(`API returned ${response.status}`);
      setResult(await response.json());
    } catch (err) { setError(String(err)); } finally { setLoading(false); }
  }
  return <main><header><small>ENTERPRISE RESEARCH · STARTER</small><h1>Multi-Agent Research Workspace</h1><p>LangGraph runtime scaffold · AWS AI-DLC integration pending</p></header><section><form onSubmit={submit}><label htmlFor="query">Research query</label><textarea id="query" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Ask about an uploaded document or current web information" required maxLength={4000}/><button disabled={loading}>{loading ? 'Running…' : 'Run demo routing'}</button></form></section>{error && <section role="alert">{error}</section>}{result && <section><div className="meta">Route: {result.route.toUpperCase()} · Mode: {result.mode.toUpperCase()}</div><h2>Result</h2><p>{result.answer}</p><h3>Adapter status</h3>{result.warnings.length ? <ul>{result.warnings.map((w,i)=><li key={i}>{w}</li>)}</ul> : <p>No adapter warnings.</p>}<p className="muted">Verified citations: {result.citations.length}</p></section>}<footer>Demo-only. No retrieval, live web search, or enterprise security has been activated.</footer></main>;
}
createRoot(document.getElementById('root')!).render(<React.StrictMode><App/></React.StrictMode>);
