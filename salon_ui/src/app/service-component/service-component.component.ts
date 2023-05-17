import { Component } from '@angular/core';
import { SalonServiceService } from '../salon-service.service';
import { Services } from '../models/models';
import { MatDialog } from '@angular/material/dialog';
import { CreateServiceComponent } from '../create-service/create-service.component';

@Component({
  selector: 'app-service-component',
  templateUrl: './service-component.component.html',
  styleUrls: ['./service-component.component.css']
})
export class ServiceComponentComponent {
  servicesAvailable: Services[] = []
  constructor(private salonService: SalonServiceService, public dialog: MatDialog) {
    this.getServices();

  }
  openDialog() {
    const dialogRef = this.dialog.open(CreateServiceComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
      this.getServices();
    });
  }
  getServices() {
    this.salonService.getServices().subscribe((services: Services[]) => this.servicesAvailable = services);
  }
}
