import { signal } from "@preact/signals";

export const errorSignal = signal(null);

export default function raiseError(message="General error", e) {
    if (e) {
        console.error(e)
        errorSignal.value = message
    }
}
