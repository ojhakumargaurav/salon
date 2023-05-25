import { Component, Input } from '@angular/core';
import { Services } from '../models/models';

@Component({
  selector: 'app-service-card',
  templateUrl: './service-card.component.html',
  styleUrls: ['./service-card.component.css']
})
export class ServiceCardComponent {
  @Input() service: Services = new Services()



}
