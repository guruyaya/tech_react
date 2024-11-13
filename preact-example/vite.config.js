import { defineConfig } from 'vite'
import preact from '@preact/preset-vite'
import { replaceCodePlugin } from "vite-plugin-replace";


export default defineConfig(({mode}) => {
  const replacements = mode == 'development' ? [{from: /settings\.json/, to: 'dev.settings.json'}] : []
   
  return {
    plugins: [
      replaceCodePlugin({replacements}), // Note: only var name is eqvivalent to {replacements: replacements}
      preact()
    ],
  }
})
