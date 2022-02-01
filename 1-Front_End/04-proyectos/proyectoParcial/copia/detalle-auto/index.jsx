//importar el index
import auto1 from "../../img/card.png";

// import auto2 from "../../img/auto.png";
// import { NavLink as Link } from "react-router-dom";


// AGREGADO PARA BORRAR EN CASO FALLA

import auto2 from "../../img/auto2.png";
import auto3 from "../../img/auto3.png";
import auto4 from "../../img/auto4.png";
import auto5 from "../../img/auto5.png";

import "boxicons" ;
import "glider-js" ;
import Glider from "glider-js";

const DetAuto = () => {


  window.addEventListener('load', function(){
    new Glider(document.querySelector('.div1__slider__imagen__lista'),{
      slidesToShow: 2,
      slidesToScroll:1,
      // draggable: true,
      dots: '.div1__slider__indicadores',
      arrows: {
      prev: '.div1__slider__imagen__siguiente',
      next: '.div1__slider__imagen__anterior'
    }

    });

    console.log("hola")

  })

  return (
    <div className="det-main">
      <div className="div1">
        <div className="div1__slider">
          <div className="div1__slider__filtro">
            <div className="btn1">Exterior</div>
            <div className="btn2">Interior</div>
          </div>
          <div className="div1__slider__imagen">

            {/* slider  */}
            <button aria-label="Anterior" className="div1__slider__imagen__anterior">
              <i class='bx bxs-skip-next-circle'></i>
            </button>

            <div className="div1__slider__imagen__lista">
                <div className="div1__slider__imagen__elemento">
                  <img src={auto1} alt="" />
                </div>
                <div className="div1__slider__imagen__elemento">
                  <img src={auto2} alt="" />
                </div>
                <div className="div1__slider__imagen__elemento">
                  <img src={auto3} alt="" />
                </div>
                <div className="div1__slider__imagen__elemento">
                  <img src={auto4} alt="" />
                </div>
            </div>


            <button aria-label="Siguiente" className="div1__slider__imagen__siguiente">
              <i class='bx bxs-skip-previous-circle' ></i>
            </button>


          </div>

          <div role="tablist" className="div1__slider__indicadores"></div>


        </div>

        <div className="div1__frm">
          <div className="div1__frm__filtro">
            <div className="btn1">Mensaje</div>
            <div className="btn2">Telefono</div>
          </div>
          <div className="div1__frm__card">
            <h2>Contacta al Vendedor</h2>
            <form action="">
              <div className="inputs">
                <input type="text" placeholder="Nombre" />
              </div>
              <div className="inputs">
                <input type="text" placeholder="Correo" />
              </div>
              <div className="inputs">
                <input type="text" placeholder="Celular" />
              </div>
              <div className="inputs">
                <textarea placeholder="Descripcion"> </textarea>
              </div>
              <div className="inputs">
                <button className="btn">CONTACTAR</button>
              </div>
            </form>
          </div>
        </div>
      </div>

      <div className="descripcion">
        <div className="descripcion__vehiculo">
          <h2>Descripcion del Vehiculo</h2>
          <div className="descripcion__vehiculo__inputs">
            <textarea name="" id="" cols="30" rows="10">
              descripción del vehículo detallado
            </textarea>
          </div>
        </div>

        <div className="descripcion__carac">
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">Marca</div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="Volkswagen" readOnly />
            </div>
          </div>
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">Modelo</div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="PASSAT CC" readOnly />
            </div>
          </div>
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">
              Categoria
            </div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="Sedan" readOnly />
            </div>
          </div>
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">
              Año Modelo
            </div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="2012" readOnly />
            </div>
          </div>
        </div>

        <div className="descripccion__carac">
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">
              Kilometraje
            </div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="80000" readOnly />
            </div>
          </div>
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">
              Transimision
            </div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="Automatica" readOnly />
            </div>
          </div>
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">
              Combustible
            </div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="Gasolina" readOnly />
            </div>
          </div>
          <div className="descripcion__carac__division">
            <div className="descripcion__carac__division__titulo">Color</div>
            <div className="descripcion__carac__division__inputs">
              <input type="text" value="Negro" readOnly />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DetAuto;

//

// const DetAuto = () => {
//   return (
//     <div className="det-main">
//       <div className="div1">
//         <div className="div1__slider">
//           <div className="div1__slider__filtro">
//             <div className="btn1">Exterior</div>
//             <div className="btn2">Interior</div>
//           </div>
//           <div className="div1__slider__imagen">
//             <img src={auto1} alt="" />
//           </div>
//         </div>

//         <div className="div1__frm">
//           <div className="div1__frm__filtro">
//             <div className="btn1">Mensaje</div>
//             <div className="btn2">Telefono</div>
//           </div>
//           <div className="div1__frm__card">
//             <h2>Contacta al Vendedor</h2>
//             <form action="">
//               <div className="inputs">
//                 <input type="text" placeholder="Nombre" />
//               </div>
//               <div className="inputs">
//                 <input type="text" placeholder="Correo" />
//               </div>
//               <div className="inputs">
//                 <input type="text" placeholder="Celular" />
//               </div>
//               <div className="inputs">
//                 <textarea placeholder="Descripcion"> </textarea>
//               </div>
//               <div className="inputs">
//                 <button className="btn">CONTACTAR</button>
//               </div>
//             </form>
//           </div>
//         </div>
//       </div>

//       <div className="descripcion">
//         <div className="descripcion__vehiculo">
//           <h2>Descripcion del Vehiculo</h2>
//           <div className="descripcion__vehiculo__inputs">
//             <textarea name="" id="" cols="30" rows="10">
//               descripción del vehículo detallado
//             </textarea>
//           </div>
//         </div>

//         <div className="descripcion__carac">
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">Marca</div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="Volkswagen" readOnly />
//             </div>
//           </div>
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">Modelo</div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="PASSAT CC" readOnly />
//             </div>
//           </div>
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">
//               Categoria
//             </div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="Sedan" readOnly />
//             </div>
//           </div>
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">
//               Año Modelo
//             </div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="2012" readOnly />
//             </div>
//           </div>
//         </div>

//         <div className="descripccion__carac">
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">
//               Kilometraje
//             </div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="80000" readOnly />
//             </div>
//           </div>
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">
//               Transimision
//             </div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="Automatica" readOnly />
//             </div>
//           </div>
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">
//               Combustible
//             </div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="Gasolina" readOnly />
//             </div>
//           </div>
//           <div className="descripcion__carac__division">
//             <div className="descripcion__carac__division__titulo">Color</div>
//             <div className="descripcion__carac__division__inputs">
//               <input type="text" value="Negro" readOnly />
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default DetAuto;
