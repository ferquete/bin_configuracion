import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { MiappSharedLibsModule, MiappSharedCommonModule, JhiLoginModalComponent, HasAnyAuthorityDirective } from './';

@NgModule({
  imports: [MiappSharedLibsModule, MiappSharedCommonModule],
  declarations: [JhiLoginModalComponent, HasAnyAuthorityDirective],
  entryComponents: [JhiLoginModalComponent],
  exports: [MiappSharedCommonModule, JhiLoginModalComponent, HasAnyAuthorityDirective],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MiappSharedModule {
  static forRoot() {
    return {
      ngModule: MiappSharedModule
    };
  }
}
