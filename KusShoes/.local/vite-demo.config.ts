import baseConfig from '../FE/vite.config.ts';

// Development-only same-origin API proxy. The repository config stays unchanged.
export default async (environment: Parameters<typeof baseConfig>[0]) => {
  const config = await baseConfig(environment);
  return {
    ...config,
    server: {
      host: '127.0.0.1',
      port: 5173,
      strictPort: true,
      proxy: {
        '/api': { target: 'http://127.0.0.1:8000', changeOrigin: false },
        '/health': { target: 'http://127.0.0.1:8000', changeOrigin: false },
      },
    },
  };
};
