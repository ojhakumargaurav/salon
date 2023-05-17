import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ServiceComponentComponent} from './service-component/service-component.component'

const routes: Routes = [
  {path:"services", component: ServiceComponentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
