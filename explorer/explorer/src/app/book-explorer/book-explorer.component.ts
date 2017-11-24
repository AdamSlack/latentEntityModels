import { Component, OnInit } from '@angular/core';
import { ExplorerApiService } from '../services/explorer-api.service'
import { Subscription } from 'rxjs/Subscription';
@Component({
  selector: 'app-book-explorer',
  templateUrl: './book-explorer.component.html',
  styleUrls: ['./book-explorer.component.scss']
})
export class BookExplorerComponent implements OnInit {


  // variables
  public entities : Array<string>;
  public terms : {term : string, strength : number}
  public selectedEntity : string = 'Select an Entity';

  // subscriptions
  private entitySubscription : Subscription;
  private entityTermSubscription : Subscription;

  constructor(public bookQuery : ExplorerApiService) { }

  public requestEntity(entity: string) {
    if(this.entityTermSubscription) {
      this.entityTermSubscription.unsubscribe();
    }
    this.entityTermSubscription = this.bookQuery.requestEntityTerms('alice_in_wonderland', entity).subscribe((res) => {
      this.selectedEntity = entity;
      this.terms = res.terms;
    })
  }
  
  ngOnInit() {
    this.entitySubscription = this.bookQuery.requestEntities('alice_in_wonderland').subscribe((res) => {
      this.entities = res.entities;
    })
  }

}
