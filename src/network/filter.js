import { request } from "@/network/request.js";

export function postFilterForm(data) {
  return request({
    url: '/filter',
    method: 'post',
    data: data
  })
}
