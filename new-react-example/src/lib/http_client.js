import settings from '../config/settings.json'
import axios from 'axios'


class HttpClient {
    options = {
        withCredentials: true,
        headers: {'Access-Control-Allow-Origin': '*'}
    };
    
    constructor(base_url) {
        this.base_url = base_url
    }
    get_body_form(data) {
        const formData = new FormData();
        for (const key in data) {
            console.log(key, data[key])
            formData.append(key, data[key]);
        }
        return formData;
    }

    get(url) {
        return axios.get(settings.base_url + url, this.options)
    }

    post(url, data, is_form=false) {
        const body = (is_form) ? this.get_body_form(data) : data;
        return axios.post(settings.base_url + url, body, this.options)
    }

    put(url, data) {
        return axios.put(settings.base_url + url, data, this.options)
    }

    delete(url) {
        return axios.delete(settings.base_url + url, {}, this.options)
    }
}

const httpClient = new HttpClient(settings.base_url)
export default httpClient
