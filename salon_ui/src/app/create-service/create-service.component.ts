import { Component } from '@angular/core';
import { FormBuilder, FormControl } from '@angular/forms';
import { SalonServiceService } from '../salon-service.service';

@Component({
  selector: 'app-create-service',
  templateUrl: './create-service.component.html',
  styleUrls: ['./create-service.component.css']

})
export class CreateServiceComponent {

  constructor(private salonService: SalonServiceService, private formBuilder: FormBuilder) {

  }
  nameControl = new FormControl("")
  descriptionControl = new FormControl("")
  priceControl = new FormControl(100)
  imageurlControl = new FormControl("")
  servicesForm = this.formBuilder.group({
    name: this.nameControl,
    description: this.descriptionControl,
    price: this.priceControl,
    image_url: this.imageurlControl

  })

  createNewService() {
    console.log(this.servicesForm.value);
    this.salonService.setServices(this.servicesForm.getRawValue()).subscribe(data => {
      console.log(data)
    });

  }

}
