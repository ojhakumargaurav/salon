import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Services } from './models/models';
const backend_url = "http://localhost:8000/salon"

@Injectable({
  providedIn: 'root'
})
export class SalonServiceService {
  private services: Services[] = [];

  constructor(private http: HttpClient) { }
  getServices() {
    return this.http.get<Services[]>(backend_url + "/service");
  }
  setServices(service: any) {
    return this.http.post(backend_url + "/service/", service);

  }
}
