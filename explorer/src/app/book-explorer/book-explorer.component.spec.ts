import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BookExplorerComponent } from './book-explorer.component';

describe('BookExplorerComponent', () => {
  let component: BookExplorerComponent;
  let fixture: ComponentFixture<BookExplorerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BookExplorerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BookExplorerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
