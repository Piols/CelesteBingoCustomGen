__all__ = ['slrv5']

#This code is unreadable, don't try, just use
# from slrv5 import slrv5
# slrv5.genBoardSlrv5(json, seed)

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['genBoardSlrv5'])
@Js
def PyJsHoisted_genBoardSlrv5_(bingoList, seed, this, arguments, var=var):
    var = Scope({'bingoList':bingoList, 'seed':seed, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'i', 'synergy', 'lineCheckList', 'SEED', 'RNG', 'minSynObj', 'bingoList', 'seed', 'size', 'MAX_SEED', 'currentObj', 'bingoBoard', 'difficulty', 'checkLine', 'getDifficulty'])
    @Js
    def PyJsHoisted_difficulty_(i, this, arguments, var=var):
        var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['Table1', 'i', 'value', 'Table5', 'x', 'y', 'RemT', 'e1', 'Rem3', 'Rem8', 'Num3', 'Rem5', 'e5', 'Rem4', 'Rem2'])
        var.put('Num3', (var.get('SEED')%Js(1000.0)))
        var.put('Rem8', (var.get('Num3')%Js(8.0)))
        var.put('Rem4', var.get('Math').callprop('floor', (var.get('Rem8')/Js(2.0))))
        var.put('Rem2', (var.get('Rem8')%Js(2.0)))
        var.put('Rem5', (var.get('Num3')%Js(5.0)))
        var.put('Rem3', (var.get('Num3')%Js(3.0)))
        var.put('RemT', var.get('Math').callprop('floor', (var.get('Num3')/Js(120.0))))
        var.put('Table5', Js([Js(0.0)]))
        var.get('Table5').callprop('splice', var.get('Rem2'), Js(0.0), Js(1.0))
        var.get('Table5').callprop('splice', var.get('Rem3'), Js(0.0), Js(2.0))
        var.get('Table5').callprop('splice', var.get('Rem4'), Js(0.0), Js(3.0))
        var.get('Table5').callprop('splice', var.get('Rem5'), Js(0.0), Js(4.0))
        var.put('Num3', var.get('Math').callprop('floor', (var.get('SEED')/Js(1000.0))))
        var.put('Num3', (var.get('Num3')%Js(1000.0)))
        var.put('Rem8', (var.get('Num3')%Js(8.0)))
        var.put('Rem4', var.get('Math').callprop('floor', (var.get('Rem8')/Js(2.0))))
        var.put('Rem2', (var.get('Rem8')%Js(2.0)))
        var.put('Rem5', (var.get('Num3')%Js(5.0)))
        var.put('Rem3', (var.get('Num3')%Js(3.0)))
        var.put('RemT', ((var.get('RemT')*Js(8.0))+var.get('Math').callprop('floor', (var.get('Num3')/Js(120.0)))))
        var.put('Table1', Js([Js(0.0)]))
        var.get('Table1').callprop('splice', var.get('Rem2'), Js(0.0), Js(1.0))
        var.get('Table1').callprop('splice', var.get('Rem3'), Js(0.0), Js(2.0))
        var.get('Table1').callprop('splice', var.get('Rem4'), Js(0.0), Js(3.0))
        var.get('Table1').callprop('splice', var.get('Rem5'), Js(0.0), Js(4.0))
        (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))
        var.put('RemT', (var.get('RemT')%Js(5.0)))
        var.put('x', ((var.get('i')+var.get('RemT'))%Js(5.0)))
        var.put('y', var.get('Math').callprop('floor', (var.get('i')/Js(5.0))))
        var.put('e5', var.get('Table5').get(((var.get('x')+(Js(3.0)*var.get('y')))%Js(5.0))))
        var.put('e1', var.get('Table1').get((((Js(3.0)*var.get('x'))+var.get('y'))%Js(5.0))))
        var.put('value', ((Js(5.0)*var.get('e5'))+var.get('e1')))
        (var.put('value',Js(var.get('value').to_number())+Js(1))-Js(1))
        return var.get('value')
    PyJsHoisted_difficulty_.func_name = 'difficulty'
    var.put('difficulty', PyJsHoisted_difficulty_)
    @Js
    def PyJsHoisted_checkLine_(i, typesA, this, arguments, var=var):
        var = Scope({'i':i, 'typesA':typesA, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'typesA', 'synergy', 'k', 'j', 'typesB'])
        var.put('synergy', Js(0.0))
        #for JS loop
        var.put('j', Js(0.0))
        while (var.get('j')<var.get('lineCheckList').get(var.get('i')).get('length')):
            try:
                var.put('typesB', var.get('bingoBoard').get((var.get('lineCheckList').get(var.get('i')).get(var.get('j'))+Js(1.0))).get('types'))
                if ((var.get('typesA',throw=False).typeof()!=Js('undefined')) and (var.get('typesB',throw=False).typeof()!=Js('undefined'))):
                    #for JS loop
                    var.put('k', Js(0.0))
                    while (var.get('k')<var.get('typesA').get('length')):
                        try:
                            #for JS loop
                            var.put('l', Js(0.0))
                            while (var.get('l')<var.get('typesB').get('length')):
                                try:
                                    if (var.get('typesA').get(var.get('k'))==var.get('typesB').get(var.get('l'))):
                                        (var.put('synergy',Js(var.get('synergy').to_number())+Js(1))-Js(1))
                                        if (var.get('k')==Js(0.0)):
                                            (var.put('synergy',Js(var.get('synergy').to_number())+Js(1))-Js(1))
                                        pass
                                        if (var.get('l')==Js(0.0)):
                                            (var.put('synergy',Js(var.get('synergy').to_number())+Js(1))-Js(1))
                                        pass
                                finally:
                                        (var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))
                        finally:
                                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
            finally:
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        return var.get('synergy')
    PyJsHoisted_checkLine_.func_name = 'checkLine'
    var.put('checkLine', PyJsHoisted_checkLine_)
    if (var.get('seed')==Js('')):
        var.put('seed', var.get('Math').callprop('ceil', (Js(999999.0)*var.get('Math').callprop('random'))))
    var.put('SEED', var.get('seed').callprop('toString'))
    var.put('size', Js(5.0))
    if Js(True):
        var.get('Math').callprop('seedrandom', var.get('SEED'))
        var.put('MAX_SEED', Js(999999.0))
        var.put('lineCheckList', Js([]))
        if (var.get('size')==Js(5.0)):
            var.get('lineCheckList').put('1', Js([Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(10.0), Js(15.0), Js(20.0), Js(6.0), Js(12.0), Js(18.0), Js(24.0)]))
            var.get('lineCheckList').put('2', Js([Js(0.0), Js(2.0), Js(3.0), Js(4.0), Js(6.0), Js(11.0), Js(16.0), Js(21.0)]))
            var.get('lineCheckList').put('3', Js([Js(0.0), Js(1.0), Js(3.0), Js(4.0), Js(7.0), Js(12.0), Js(17.0), Js(22.0)]))
            var.get('lineCheckList').put('4', Js([Js(0.0), Js(1.0), Js(2.0), Js(4.0), Js(8.0), Js(13.0), Js(18.0), Js(23.0)]))
            var.get('lineCheckList').put('5', Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(8.0), Js(12.0), Js(16.0), Js(20.0), Js(9.0), Js(14.0), Js(19.0), Js(24.0)]))
            var.get('lineCheckList').put('6', Js([Js(0.0), Js(10.0), Js(15.0), Js(20.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0)]))
            var.get('lineCheckList').put('7', Js([Js(0.0), Js(12.0), Js(18.0), Js(24.0), Js(5.0), Js(7.0), Js(8.0), Js(9.0), Js(1.0), Js(11.0), Js(16.0), Js(21.0)]))
            var.get('lineCheckList').put('8', Js([Js(5.0), Js(6.0), Js(8.0), Js(9.0), Js(2.0), Js(12.0), Js(17.0), Js(22.0)]))
            var.get('lineCheckList').put('9', Js([Js(4.0), Js(12.0), Js(16.0), Js(20.0), Js(9.0), Js(7.0), Js(6.0), Js(5.0), Js(3.0), Js(13.0), Js(18.0), Js(23.0)]))
            var.get('lineCheckList').put('10', Js([Js(4.0), Js(14.0), Js(19.0), Js(24.0), Js(8.0), Js(7.0), Js(6.0), Js(5.0)]))
            var.get('lineCheckList').put('11', Js([Js(0.0), Js(5.0), Js(15.0), Js(20.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0)]))
            var.get('lineCheckList').put('12', Js([Js(1.0), Js(6.0), Js(16.0), Js(21.0), Js(10.0), Js(12.0), Js(13.0), Js(14.0)]))
            var.get('lineCheckList').put('13', Js([Js(0.0), Js(6.0), Js(12.0), Js(18.0), Js(24.0), Js(20.0), Js(16.0), Js(8.0), Js(4.0), Js(2.0), Js(7.0), Js(17.0), Js(22.0), Js(10.0), Js(11.0), Js(13.0), Js(14.0)]))
            var.get('lineCheckList').put('14', Js([Js(3.0), Js(8.0), Js(18.0), Js(23.0), Js(10.0), Js(11.0), Js(12.0), Js(14.0)]))
            var.get('lineCheckList').put('15', Js([Js(4.0), Js(9.0), Js(19.0), Js(24.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0)]))
            var.get('lineCheckList').put('16', Js([Js(0.0), Js(5.0), Js(10.0), Js(20.0), Js(16.0), Js(17.0), Js(18.0), Js(19.0)]))
            var.get('lineCheckList').put('17', Js([Js(15.0), Js(17.0), Js(18.0), Js(19.0), Js(1.0), Js(6.0), Js(11.0), Js(21.0), Js(20.0), Js(12.0), Js(8.0), Js(4.0)]))
            var.get('lineCheckList').put('18', Js([Js(15.0), Js(16.0), Js(18.0), Js(19.0), Js(2.0), Js(7.0), Js(12.0), Js(22.0)]))
            var.get('lineCheckList').put('19', Js([Js(15.0), Js(16.0), Js(17.0), Js(19.0), Js(23.0), Js(13.0), Js(8.0), Js(3.0), Js(24.0), Js(12.0), Js(6.0), Js(0.0)]))
            var.get('lineCheckList').put('20', Js([Js(4.0), Js(9.0), Js(14.0), Js(24.0), Js(15.0), Js(16.0), Js(17.0), Js(18.0)]))
            var.get('lineCheckList').put('21', Js([Js(0.0), Js(5.0), Js(10.0), Js(15.0), Js(16.0), Js(12.0), Js(8.0), Js(4.0), Js(21.0), Js(22.0), Js(23.0), Js(24.0)]))
            var.get('lineCheckList').put('22', Js([Js(20.0), Js(22.0), Js(23.0), Js(24.0), Js(1.0), Js(6.0), Js(11.0), Js(16.0)]))
            var.get('lineCheckList').put('23', Js([Js(2.0), Js(7.0), Js(12.0), Js(17.0), Js(20.0), Js(21.0), Js(23.0), Js(24.0)]))
            var.get('lineCheckList').put('24', Js([Js(20.0), Js(21.0), Js(22.0), Js(24.0), Js(3.0), Js(8.0), Js(13.0), Js(18.0)]))
            var.get('lineCheckList').put('25', Js([Js(0.0), Js(6.0), Js(12.0), Js(18.0), Js(20.0), Js(21.0), Js(22.0), Js(23.0), Js(19.0), Js(14.0), Js(9.0), Js(4.0)]))
        pass
        pass
        var.put('bingoBoard', Js([]))
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<=Js(25.0)):
            try:
                var.get('bingoBoard').put(var.get('i'), Js({'difficulty':var.get('difficulty')(var.get('i'))}))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<=Js(25.0)):
            try:
                var.put('getDifficulty', var.get('bingoBoard').get(var.get('i')).get('difficulty'))
                var.put('RNG', var.get('Math').callprop('floor', (var.get('bingoList').get(var.get('getDifficulty')).get('length')*var.get('Math').callprop('random'))))
                if (var.get('RNG')==var.get('bingoList').get(var.get('getDifficulty')).get('length')):
                    (var.put('RNG',Js(var.get('RNG').to_number())-Js(1))+Js(1))
                pass
                var.put('j', Js(0.0))
                var.put('synergy', Js(0.0))
                var.put('currentObj', var.get(u"null"))
                var.put('minSynObj', var.get(u"null"))
                while 1:
                    var.put('currentObj', var.get('bingoList').get(var.get('getDifficulty')).get(((var.get('j')+var.get('RNG'))%var.get('bingoList').get(var.get('getDifficulty')).get('length'))))
                    var.put('synergy', var.get('checkLine')(var.get('i'), var.get('currentObj').get('types')))
                    if ((var.get('minSynObj')==var.get(u"null")) or (var.get('synergy')<var.get('minSynObj').get('synergy'))):
                        var.put('minSynObj', Js({'synergy':var.get('synergy'),'value':var.get('currentObj'),'id':((var.get('j')+var.get('RNG'))%var.get('bingoList').get(var.get('getDifficulty')).get('length'))}))
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    if not ((var.get('synergy')!=Js(0.0)) and (var.get('j')<var.get('bingoList').get(var.get('getDifficulty')).get('length'))):
                        break
                var.get('bingoBoard').get(var.get('i')).put('types', var.get('minSynObj').get('value').get('types'))
                var.get('bingoBoard').get(var.get('i')).put('name', var.get('minSynObj').get('value').get('name'))
                var.get('bingoBoard').get(var.get('i')).put('tier', var.get('getDifficulty'))
                var.get('bingoBoard').get(var.get('i')).put('id', var.get('minSynObj').get('id'))
                var.get('bingoBoard').get(var.get('i')).put('synergy', var.get('minSynObj').get('synergy'))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('bingoBoard')
PyJsHoisted_genBoardSlrv5_.func_name = 'genBoardSlrv5'
var.put('genBoardSlrv5', PyJsHoisted_genBoardSlrv5_)
@Js
def PyJs_anonymous_0_(j, i, g, m, k, n, o, this, arguments, var=var):
    var = Scope({'j':j, 'i':i, 'g':g, 'm':m, 'k':k, 'n':n, 'o':o, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'o', 'm', 'l', 'g', 'q', 'p', 'k', 'j', 'n'])
    @Js
    def PyJsHoisted_q_(b, this, arguments, var=var):
        var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['d', 'b', 'c', 'h', 'f', 'e', 'a'])
        var.put('a', var.get(u"this"))
        var.put('c', var.get('b').get('length'))
        var.put('d', Js(0.0))
        var.put('h', var.get('a').put('i', var.get('a').put('j', var.get('a').put('m', Js(0.0)))))
        var.get('a').put('S', Js([]))
        var.get('a').put('c', Js([]))
        #for JS loop
        (var.get('c') or var.put('b', Js([(var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))])))
        while (var.get('d')<var.get('g')):
            var.get('a').get('S').put(var.get('d'), (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)))
        
        #for JS loop
        var.put('d', Js(0.0))
        while (var.get('d')<var.get('g')):
            try:
                PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('e', var.get('a').get('S').get(var.get('d'))),var.put('h', (((var.get('h')+var.get('e'))+var.get('b').get((var.get('d')%var.get('c'))))&(var.get('g')-Js(1.0))))),var.put('f', var.get('a').get('S').get(var.get('h')))),var.get('a').get('S').put(var.get('d'), var.get('f'))),var.get('a').get('S').put(var.get('h'), var.get('e')))
            finally:
                    (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
        @Js
        def PyJs_anonymous_1_(b, this, arguments, var=var):
            var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['d', 'i', 'c', 'h', 'f', 'e', 'b'])
            var.put('c', var.get('a').get('S'))
            var.put('d', ((var.get('a').get('i')+Js(1.0))&(var.get('g')-Js(1.0))))
            var.put('e', var.get('c').get(var.get('d')))
            var.put('f', ((var.get('a').get('j')+var.get('e'))&(var.get('g')-Js(1.0))))
            var.put('h', var.get('c').get(var.get('f')))
            var.get('c').put(var.get('d'), var.get('h'))
            var.get('c').put(var.get('f'), var.get('e'))
            #for JS loop
            var.put('i', var.get('c').get(((var.get('e')+var.get('h'))&(var.get('g')-Js(1.0)))))
            while var.put('b',Js(var.get('b').to_number())-Js(1)):
                def PyJs_LONG_2_(var=var):
                    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('d', ((var.get('d')+Js(1.0))&(var.get('g')-Js(1.0)))),var.put('e', var.get('c').get(var.get('d')))),var.put('f', ((var.get('f')+var.get('e'))&(var.get('g')-Js(1.0))))),var.put('h', var.get('c').get(var.get('f')))),var.get('c').put(var.get('d'), var.get('h'))),var.get('c').put(var.get('f'), var.get('e'))),var.put('i', ((var.get('i')*var.get('g'))+var.get('c').get(((var.get('e')+var.get('h'))&(var.get('g')-Js(1.0)))))))
                PyJs_LONG_2_()
            
            var.get('a').put('i', var.get('d'))
            var.get('a').put('j', var.get('f'))
            return var.get('i')
        PyJs_anonymous_1_._set_name('anonymous')
        var.get('a').put('g', PyJs_anonymous_1_)
        var.get('a').callprop('g', var.get('g'))
    PyJsHoisted_q_.func_name = 'q'
    var.put('q', PyJsHoisted_q_)
    @Js
    def PyJsHoisted_p_(b, e, f, a, c, this, arguments, var=var):
        var = Scope({'b':b, 'e':e, 'f':f, 'a':a, 'c':c, 'this':this, 'arguments':arguments}, var)
        var.registers(['c', 'a', 'f', 'e', 'b'])
        var.put('f', Js([]))
        var.put('c', var.get('b',throw=False).typeof())
        if (var.get('e') and (var.get('c')==Js('object'))):
            for PyJsTemp in var.get('b'):
                var.put('a', PyJsTemp)
                if (var.get('a').callprop('indexOf', Js('S'))<Js(5.0)):
                    try:
                        var.get('f').callprop('push', var.get('p')(var.get('b').get(var.get('a')), (var.get('e')-Js(1.0))))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_64_55070682 = var.own.get('d')
                        var.force_own_put('d', PyExceptionToJs(PyJsTempException))
                        try:
                            pass
                        finally:
                            if PyJsHolder_64_55070682 is not None:
                                var.own['d'] = PyJsHolder_64_55070682
                            else:
                                del var.own['d']
                            del PyJsHolder_64_55070682
        return (var.get('f') if var.get('f').get('length') else (var.get('b')+(Js('\x00') if (var.get('c')!=Js('string')) else Js(''))))
    PyJsHoisted_p_.func_name = 'p'
    var.put('p', PyJsHoisted_p_)
    @Js
    def PyJsHoisted_l_(b, e, f, a, this, arguments, var=var):
        var = Scope({'b':b, 'e':e, 'f':f, 'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['d', 'c', 'h', 'a', 'f', 'e', 'b'])
        var.put('b', Js(''), '+')
        #for JS loop
        var.put('a', var.put('f', Js(0.0)))
        while (var.get('a')<var.get('b').get('length')):
            try:
                var.put('c', var.get('e'))
                var.put('d', (var.get('a')&(var.get('g')-Js(1.0))))
                var.put('h', (var.put('f', (var.get('e').get((var.get('a')&(var.get('g')-Js(1.0))))*Js(19.0)), '^')+var.get('b').callprop('charCodeAt', var.get('a'))))
                var.get('c').put(var.get('d'), (var.get('h')&(var.get('g')-Js(1.0))))
            finally:
                    (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
        var.put('b', Js(''))
        for PyJsTemp in var.get('e'):
            var.put('a', PyJsTemp)
            var.put('b', var.get('String').callprop('fromCharCode', var.get('e').get(var.get('a'))), '+')
        return var.get('b')
    PyJsHoisted_l_.func_name = 'l'
    var.put('l', PyJsHoisted_l_)
    pass
    pass
    pass
    @Js
    def PyJs_anonymous_3_(b, e, this, arguments, var=var):
        var = Scope({'b':b, 'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 'f', 'e', 'a'])
        var.put('f', Js([]))
        var.put('b', var.get('l')(var.get('p')((Js([var.get('b'), var.get('j')]) if var.get('e') else (var.get('b') if var.get('arguments').get('length') else Js([var.get('Date').create().callprop('getTime'), var.get('j'), var.get('window')]))), Js(3.0)), var.get('f')))
        var.put('a', var.get('q').create(var.get('f')))
        var.get('l')(var.get('a').get('S'), var.get('j'))
        @Js
        def PyJs_anonymous_4_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['d', 'c', 'b'])
            #for JS loop
            var.put('c', var.get('a').callprop('g', var.get('m')))
            var.put('d', var.get('o'))
            var.put('b', Js(0.0))
            while (var.get('c')<var.get('k')):
                PyJsComma(PyJsComma(var.put('c', ((var.get('c')+var.get('b'))*var.get('g'))),var.put('d', var.get('g'), '*')),var.put('b', var.get('a').callprop('g', Js(1.0))))
            
            #for JS loop
            
            while (var.get('c')>=var.get('n')):
                PyJsComma(PyJsComma(var.put('c', Js(2.0), '/'),var.put('d', Js(2.0), '/')),var.put('b', Js(1.0), '>>>'))
            
            return ((var.get('c')+var.get('b'))/var.get('d'))
        PyJs_anonymous_4_._set_name('anonymous')
        var.get('i').put('random', PyJs_anonymous_4_)
        return var.get('b')
    PyJs_anonymous_3_._set_name('anonymous')
    var.get('i').put('seedrandom', PyJs_anonymous_3_)
    var.put('o', var.get('i').callprop('pow', var.get('g'), var.get('m')))
    var.put('k', var.get('i').callprop('pow', Js(2.0), var.get('k')))
    var.put('n', (var.get('k')*Js(2.0)))
    var.get('l')(var.get('i').callprop('random'), var.get('j'))
PyJs_anonymous_0_._set_name('anonymous')
PyJs_anonymous_0_(Js([]), var.get('Math'), Js(256.0), Js(6.0), Js(52.0))
pass
pass


# Add lib to the module scope
slrv5 = var.to_python()