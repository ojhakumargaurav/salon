import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServiceComponentComponent } from './service-component.component';

describe('ServiceComponentComponent', () => {
  let component: ServiceComponentComponent;
  let fixture: ComponentFixture<ServiceComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ServiceComponentComponent]
    });
    fixture = TestBed.createComponent(ServiceComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
