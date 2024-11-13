import { createSignal } from 'react-use-signals';

export const errorSignal = createSignal(null);

export default function raiseError(message="General error", e) {
    if (e) {
        console.error(e)
        errorSignal.value = message
    }
}
