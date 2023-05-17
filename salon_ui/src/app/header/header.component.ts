import { Component, inject, Input } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  private breakpointObserver = inject(BreakpointObserver);
  @Input() title:string=""
  ngOnInit(){
    
    
  }

  isHandset$: Observable<boolean> = this.breakpointObserver.observe([Breakpoints.Handset, Breakpoints.Web])
    .pipe(
      map(result =>{ 
        console.log(result)
        return result.matches}),
      shareReplay()
    );
}
