import { request } from "@/network/request.js";

export function postFilterForm(data) {
  return request({
    url: '/api/search',
    method: 'post',
    data: data
  })
}
