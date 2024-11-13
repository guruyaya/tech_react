import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { replaceCodePlugin } from "vite-plugin-replace";

// This is the original condfig
// // https://vite.dev/config/
// export default defineConfig({
//   plugins: [react()],
// })

export default defineConfig(({mode}) => {
  const replacements = mode == 'development' ? [{from: /settings\.json/, to: 'dev.settings.json'}] : []
   
  return {
    plugins: [
      replaceCodePlugin({replacements}), // Note: only var name is eqvivalent to {replacements: replacements}
      react()
    ],
  }
})
